import { createMemoryRouter, RouterProvider } from 'react-router';
import { QueryClientProvider } from '@tanstack/react-query';
import { render, screen } from '@testing-library/react';
import fetchMock from 'fetch-mock';
import { IntlProvider } from 'react-intl';

import { CunninghamProvider } from '@openfun/cunningham-react';
import { capitalize } from 'lodash-es';
import {
  RichieContextFactory as mockRichieContextFactory,
  UserFactory,
} from 'utils/test/factories/richie';
import JoanieSessionProvider from 'contexts/SessionContext/JoanieSessionProvider';
import { OfferFactory, OrganizationFactory } from 'utils/test/factories/joanie';
import { createTestQueryClient } from 'utils/test/createTestQueryClient';
import { expectNoSpinner } from 'utils/test/expectSpinner';
import { DashboardBreadcrumbsProvider } from 'widgets/Dashboard/contexts/DashboardBreadcrumbsContext';
import { TeacherDashboardTrainingLoader } from '.';

jest.mock('utils/context', () => ({
  __esModule: true,
  default: mockRichieContextFactory({
    authentication: { backend: 'fonzie', endpoint: 'https://demo.endpoint' },
    joanie_backend: { endpoint: 'https://joanie.endpoint' },
  }).one(),
}));

jest.mock('hooks/useIntersectionObserver', () => ({
  useIntersectionObserver: (props: any) => {
    (globalThis as any).__intersection_observer_props__ = props;
  },
}));

describe('components/TeacherDashboardTrainingLoader', () => {
  let nbApiCalls: number;
  beforeEach(() => {
    // Joanie providers calls
    fetchMock.get('https://joanie.endpoint/api/v1.0/orders/', []);
    fetchMock.get('https://joanie.endpoint/api/v1.0/credit-cards/', []);
    fetchMock.get('https://joanie.endpoint/api/v1.0/addresses/', []);
    nbApiCalls = 3;
  });

  afterEach(() => {
    fetchMock.restore();
  });

  it('should render TeacherDashboardTrainingLoader page', async () => {
    const offer = OfferFactory().one();
    fetchMock.get(`https://joanie.endpoint/api/v1.0/organizations/?offer_id=${offer.id}`, []);
    fetchMock.get(`https://joanie.endpoint/api/v1.0/offers/${offer.id}/`, offer);

    const user = UserFactory().one();
    render(
      <IntlProvider locale="en">
        <QueryClientProvider client={createTestQueryClient({ user })}>
          <JoanieSessionProvider>
            <DashboardBreadcrumbsProvider>
              <CunninghamProvider>
                <RouterProvider
                  router={createMemoryRouter(
                    [
                      {
                        path: ':offerId',
                        element: <TeacherDashboardTrainingLoader />,
                      },
                    ],
                    {
                      initialEntries: [`/${offer.id}`],
                    },
                  )}
                />
              </CunninghamProvider>
            </DashboardBreadcrumbsProvider>
          </JoanieSessionProvider>
        </QueryClientProvider>
      </IntlProvider>,
    );
    // page placeholder
    await expectNoSpinner('Loading training...');
    // sidebar placeholder
    await expectNoSpinner('Loading course...');

    nbApiCalls += 1; // organizations api call
    nbApiCalls += 1; // offers api call
    const calledUrls = fetchMock.calls().map((call) => call[0]);
    expect(calledUrls).toHaveLength(nbApiCalls);
    expect(calledUrls).toContain(`https://joanie.endpoint/api/v1.0/offers/${offer.id}/`);

    // main titles
    expect(
      screen.getByRole('heading', {
        name: 'Training area',
      }),
    ).toBeInTheDocument();

    expect(screen.getAllByRole('heading', { name: capitalize(offer.product.title) })).toHaveLength(
      2,
    );

    const nbCourseRun = offer.product.target_courses.reduce(
      (acc, course) => acc + course.course_runs.length,
      0,
    );
    expect(screen.getAllByRole('link', { name: 'Go to course area' })).toHaveLength(nbCourseRun);
  });

  it('should fetch offer with organization id if there is one in the path', async () => {
    const organization = OrganizationFactory().one();
    const offer = OfferFactory({
      organizations: [organization],
    }).one();
    fetchMock.get(
      `https://joanie.endpoint/api/v1.0/organizations/${organization.id}/offers/${offer.id}/`,
      offer,
    );
    fetchMock.get(
      `https://joanie.endpoint/api/v1.0/organizations/${organization.id}/contracts/?offer_id=${offer.id}&signature_state=half_signed&page=1&page_size=25`,
      [],
    );

    const user = UserFactory().one();
    render(
      <IntlProvider locale="en">
        <QueryClientProvider client={createTestQueryClient({ user })}>
          <JoanieSessionProvider>
            <DashboardBreadcrumbsProvider>
              <CunninghamProvider>
                <RouterProvider
                  router={createMemoryRouter(
                    [
                      {
                        path: '/:organizationId/:offerId',
                        element: <TeacherDashboardTrainingLoader />,
                      },
                    ],
                    {
                      initialEntries: [`/${organization.id}/${offer.id}`],
                    },
                  )}
                />
              </CunninghamProvider>
            </DashboardBreadcrumbsProvider>
          </JoanieSessionProvider>
        </QueryClientProvider>
      </IntlProvider>,
    );
    // page placeholder
    await expectNoSpinner('Loading training...');
    // sidebar placeholder
    await expectNoSpinner('Loading course...');

    nbApiCalls += 1; // contracts api call
    nbApiCalls += 1; // offers api call
    const calledUrls = fetchMock.calls().map((call) => call[0]);
    expect(calledUrls).toHaveLength(nbApiCalls);
    expect(calledUrls).toContain(
      `https://joanie.endpoint/api/v1.0/organizations/${organization.id}/offers/${offer.id}/`,
    );

    // main titles
    expect(
      screen.getByRole('heading', {
        name: 'Training area',
      }),
    ).toBeInTheDocument();

    expect(screen.getAllByRole('heading', { name: capitalize(offer.product.title) })).toHaveLength(
      2,
    );

    const nbCourseRun = offer.product.target_courses.reduce(
      (acc, course) => acc + course.course_runs.length,
      0,
    );
    expect(screen.getAllByRole('link', { name: 'Go to course area' })).toHaveLength(nbCourseRun);
  });
});
