import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbvue/build/css/mdb.css';
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueApexCharts from 'vue-apexcharts'
import store from './store'

Vue.use(VueApexCharts)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
