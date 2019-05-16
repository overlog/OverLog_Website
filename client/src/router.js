import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import BoxPlot from "./components/BoxPlot";
import LineChart from "./components/LineChart.vue";
import Developers from "./components/Developers.vue";
import Login from "./components/Login.vue";
import Register from "./components/Register.vue";
import SearchLog from "./components/SearchLog.vue";
import AlertAlarm from "./components/AlertAlarm.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/boxplot",
      name: "boxplot",
      component: BoxPlot
    },
    {
      path: "/linechart",
      name: "linechart",
      component: LineChart
    },
    {
      path: "/developers",
      name: "develoers",
      component: Developers
    },
    {
      path: "/login",
      name: "login",
      component: Login
    },
    {
      path: "/register",
      name: "register",
      component: Register
    },
    {
      path: "/searchlog",
      name: "searchlog",
      component: SearchLog
    },
    {
      path: "/alert",
      name: "alert",
      component: AlertAlarm
    }
  ]
});
