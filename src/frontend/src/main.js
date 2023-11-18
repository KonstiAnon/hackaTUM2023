import { createApp } from "vue";
import { Quasar } from "quasar";

// Import icon libraries
import "@quasar/extras/material-icons/material-icons.css";

// Import Quasar css
import "quasar/src/css/index.sass";

// Global style
import "./style.css";

// Root component
import App from "./App.vue";

import router from "./router";

const app = createApp(App);
app.use(router, Quasar);

app.mount("#app");
