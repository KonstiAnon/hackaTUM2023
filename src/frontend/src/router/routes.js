const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [{path: "", component: () => import("pages/HomeView.vue")}],
  },
  {
    path: "/allergies",
    component: () => import("layouts/MainLayout.vue"),
    children: [{path: "", component: () => import("pages/AllergiesView.vue")}],
  },
  {
    path: "/skill",
    component: () => import("layouts/MainLayout.vue"),
    children: [{path: "", component: () => import("pages/SkillView.vue")}],
  },
  {
    path: "/tinder",
    component: () => import("layouts/MainLayout.vue"),
    children: [{path: "", component: () => import("pages/TinderView.vue")}],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
