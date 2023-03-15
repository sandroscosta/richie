import { defineMessages } from 'react-intl';

/**
 * All existing dashboard paths.
 */
export enum LearnerDashboardPaths {
  COURSES = '/courses',
  ORDER = '/courses/orders/:orderId',
  COURSE = '/courses/:code',
  PREFERENCES = '/preferences',
  PREFERENCES_ADDRESS_EDITION = '/preferences/addresses/:addressId',
  PREFERENCES_ADDRESS_CREATION = '/preferences/addresses/create',
  PREFERENCES_CREDIT_CARD_EDITION = '/preferences/credit-cards/:creditCardId',
}

// Translations of dashboard route paths
export const LEARNER_DASHBOARD_ROUTE_PATHS = defineMessages<LearnerDashboardPaths>({
  [LearnerDashboardPaths.COURSES]: {
    id: 'components.Dashboard.DashboardRoutes.courses.path',
    description: 'The path to display the courses view.',
    defaultMessage: '/courses',
  },
  [LearnerDashboardPaths.ORDER]: {
    id: 'components.Dashboard.DashboardRoutes.order.path',
    description: 'The path to display an order detail view.',
    defaultMessage: '/courses/orders/{orderId}',
  },
  [LearnerDashboardPaths.COURSE]: {
    id: 'components.Dashboard.DashboardRoutes.course.path',
    description: 'The path to display a course detail view.',
    defaultMessage: '/courses/{code}',
  },
  [LearnerDashboardPaths.PREFERENCES]: {
    id: 'components.Dashboard.DashboardRoutes.preferences.path',
    description: 'The path to display the preferences view.',
    defaultMessage: '/preferences',
  },
  [LearnerDashboardPaths.PREFERENCES_ADDRESS_EDITION]: {
    id: 'components.Dashboard.DashboardRoutes.preferences.addresses.edition.path',
    description: 'The path to display the addresses edition view.',
    defaultMessage: '/preferences/addresses/{addressId}',
  },
  [LearnerDashboardPaths.PREFERENCES_ADDRESS_CREATION]: {
    id: 'components.Dashboard.DashboardRoutes.preferences.addresses.creation.path',
    description: 'The path to display the addresses creation view.',
    defaultMessage: '/preferences/addresses/create',
  },
  [LearnerDashboardPaths.PREFERENCES_CREDIT_CARD_EDITION]: {
    id: 'components.Dashboard.DashboardRoutes.preferences.creditCards.edition.path',
    description: 'The path to display the credit cards edition view.',
    defaultMessage: '/preferences/credit-cards/{creditCardId}',
  },
});

// Translations of dashboard route labels
export const LEARNER_DASHBOARD_ROUTE_LABELS = defineMessages<LearnerDashboardPaths>({
  [LearnerDashboardPaths.COURSES]: {
    id: 'components.Dashboard.DashboardRoutes.courses.label',
    description: 'Label of the courses view used in navigation components.',
    defaultMessage: 'My courses',
  },
  [LearnerDashboardPaths.ORDER]: {
    id: 'components.Dashboard.DashboardRoutes.order.label',
    description: 'Label of the order view used in navigation components.',
    defaultMessage: '{orderTitle}',
  },
  [LearnerDashboardPaths.COURSE]: {
    id: 'components.Dashboard.DashboardRoutes.course.session.label',
    description: 'Label of the course session view used in navigation components.',
    defaultMessage: 'Course',
  },
  [LearnerDashboardPaths.PREFERENCES]: {
    id: 'components.Dashboard.DashboardRoutes.preferences.label',
    description: 'Label of the preferences view used in navigation components.',
    defaultMessage: 'My preferences',
  },
  [LearnerDashboardPaths.PREFERENCES_ADDRESS_EDITION]: {
    id: 'components.Dashboard.DashboardRoutes.preferences.addresses.edition.label',
    description: 'Label of the addresses edition view.',
    defaultMessage: 'Edit address "{addressTitle}"',
  },
  [LearnerDashboardPaths.PREFERENCES_ADDRESS_CREATION]: {
    id: 'components.Dashboard.DashboardRoutes.preferences.addresses.creation.label',
    description: 'Label of the addresses creation view.',
    defaultMessage: 'Create address',
  },
  [LearnerDashboardPaths.PREFERENCES_CREDIT_CARD_EDITION]: {
    id: 'components.Dashboard.DashboardRoutes.preferences.creditCards.label',
    description: 'Label of the credit cards edition view.',
    defaultMessage: 'Edit credit card "{creditCardTitle}"',
  },
});