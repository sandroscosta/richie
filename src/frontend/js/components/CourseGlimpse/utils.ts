import { IntlShape } from 'react-intl';
import { generatePath } from 'react-router';
import { Course as RichieCourse, isRichieCourse } from 'types/Course';
import {
  CourseListItem as JoanieCourse,
  CourseProductRelationLight,
  isCourseProductRelation,
} from 'types/Joanie';
import { TeacherDashboardPaths } from 'widgets/Dashboard/utils/teacherDashboardPaths';
import { CourseGlimpseCourse } from '.';

const getCourseGlimpsePropsFromCourseProductRelation = (
  courseProductRelation: CourseProductRelationLight,
  intl: IntlShape,
  organizationId?: string,
): CourseGlimpseCourse => {
  const courseRouteParams = {
    courseId: courseProductRelation.course.id,
    courseProductRelationId: courseProductRelation.id,
  };
  const courseRoute = organizationId
    ? generatePath(TeacherDashboardPaths.ORGANIZATION_PRODUCT, {
        ...courseRouteParams,
        organizationId,
      })
    : generatePath(TeacherDashboardPaths.COURSE_PRODUCT, courseRouteParams);
  return {
    id: courseProductRelation.id,
    code: courseProductRelation.course.code,
    title: courseProductRelation.product.title,
    cover_image: courseProductRelation.course.cover
      ? {
          src: courseProductRelation.course.cover.src,
        }
      : null,
    organization: {
      title: courseProductRelation.organizations[0].title,
      image: courseProductRelation.organizations[0].logo || null,
    },
    product_id: courseProductRelation.product.id,
    course_route: courseRoute,
    state: courseProductRelation.product.state,
  };
};

const getCourseGlimpsePropsFromRichieCourse = (course: RichieCourse): CourseGlimpseCourse => ({
  id: course.id,
  code: course.code,
  course_url: course.absolute_url,
  cover_image: course.cover_image,
  title: course.title,
  organization: {
    title: course.organization_highlighted,
    image: course.organization_highlighted_cover_image,
  },
  icon: course.icon,
  state: course.state,
  duration: course.duration,
  effort: course.effort,
  categories: course.categories,
  organizations: course.organizations,
});

const getCourseGlimpsePropsFromJoanieCourse = (
  course: JoanieCourse,
  intl: IntlShape,
  organizationId?: string,
): CourseGlimpseCourse => {
  const courseRouteParams = {
    courseId: course.id,
  };
  const courseRoute = organizationId
    ? generatePath(TeacherDashboardPaths.ORGANIZATION_COURSE_GENERAL_INFORMATION, {
        ...courseRouteParams,
        organizationId,
      })
    : generatePath(TeacherDashboardPaths.COURSE_GENERAL_INFORMATION, courseRouteParams);
  return {
    id: course.id,
    code: course.code,
    course_route: courseRoute,
    cover_image: course.cover
      ? {
          src: course.cover.src,
        }
      : null,
    title: course.title,
    organization: {
      title: course.organizations[0].title,
      image: course.organizations[0].logo || null,
    },
    state: course.state,
    nb_course_runs: course.course_run_ids.length,
  };
};

export const getCourseGlimpseProps = (
  course: RichieCourse | (JoanieCourse | CourseProductRelationLight),
  intl?: IntlShape,
  organizationId?: string,
): CourseGlimpseCourse => {
  if (isCourseProductRelation(course)) {
    return getCourseGlimpsePropsFromCourseProductRelation(course, intl!, organizationId);
  }

  if (isRichieCourse(course)) {
    return getCourseGlimpsePropsFromRichieCourse(course);
  }

  return getCourseGlimpsePropsFromJoanieCourse(course, intl!, organizationId);
};
