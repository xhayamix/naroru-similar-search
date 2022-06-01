import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import "jquery";
import "bootstrap";
import "popper.js";
import "bootstrap/dist/css/bootstrap.min.css";
import v3b4 from 'vue3-bootstrap4';

createApp(App).use(router, v3b4).mount('#app')
