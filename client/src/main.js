import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbvue/build/css/mdb.css";
import Vue from "vue";
import App from "./App.vue";
import Vuex from "vuex";
import router from "./router";
import VueApexCharts from "vue-apexcharts";
import store from "./store";
import AlertRow from "./components/AlertRow.vue";
import Axios from "axios";
import LineChart from "./components/LineChart.vue";
import SearchLog from "./components/SearchLog.vue";
import AlertAlarm from "./components/AlertAlarm.vue";
import Developers from "./components/Developers.vue";
import Login from "./components/Login.vue";
import Dashboard from "./components/Dashboard.vue";
import BoxPlot from "./components/BoxPlot.vue";
import PieChart from "./components/PieChart.vue";

import createPersistedState from "vuex-persistedstate";

Vue.prototype.$http = Axios;
const token = localStorage.getItem("token");
if (token) {
  Vue.prototype.$http.defaults.headers.common["Authorization"] = token;
}

Vue.use(VueApexCharts);
Vue.use(Vuex);

Vue.component("alert-row", AlertRow);
Vue.component("line-chart", LineChart);
Vue.component("search-log", SearchLog);
Vue.component("alert-alarm", AlertAlarm);
Vue.component("developers", Developers);
Vue.component("login", Login);
Vue.component("dashboard", Dashboard);
Vue.component("box-plot", BoxPlot);
Vue.component("pie-chart", PieChart);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
