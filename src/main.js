import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbvue/build/css/mdb.css';
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueApexCharts from 'vue-apexcharts'

Vue.use(VueApexCharts)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
