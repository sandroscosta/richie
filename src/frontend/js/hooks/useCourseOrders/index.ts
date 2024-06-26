import { defineMessages } from 'react-intl';
import { useJoanieApi } from 'contexts/JoanieApiContext';
import { useResource, useResources, UseResourcesProps, QueryOptions } from 'hooks/useResources';
import { API, CourseOrderResourceQuery, NestedCourseOrder } from 'types/Joanie';

const messages = defineMessages({
  errorGet: {
    id: 'hooks.useCourseOrders.errorSelect',
    description: 'Error message shown to the user when orders fetch request fails.',
    defaultMessage: 'An error occurred while fetching orders. Please retry later.',
  },
  errorNotFound: {
    id: 'hooks.useCourseOrders.errorNotFound',
    description: 'Error message shown to the user when no orders matches.',
    defaultMessage: 'Cannot find orders',
  },
});

const props: UseResourcesProps<
  NestedCourseOrder,
  CourseOrderResourceQuery,
  API['courses']['orders']
> = {
  queryKey: ['courses', 'orders'],
  apiInterface: () => useJoanieApi().courses.orders,
  session: true,
  messages,
};

export const useCourseOrder = (
  id: string,
  filters?: CourseOrderResourceQuery,
  queryOptions?: QueryOptions<NestedCourseOrder>,
) => {
  return useResource(props)(id, filters, {
    ...queryOptions,
    enabled:
      !!id &&
      !!filters?.organization_id &&
      (queryOptions?.enabled === undefined || queryOptions.enabled),
  });
};

export const useCourseOrders = (
  filters?: CourseOrderResourceQuery,
  queryOptions?: QueryOptions<NestedCourseOrder>,
) => {
  return useResources(props)(filters, {
    ...queryOptions,
    enabled:
      !!filters?.organization_id && (queryOptions?.enabled === undefined || queryOptions.enabled),
  });
};
