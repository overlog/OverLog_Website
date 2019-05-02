import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbvue/build/css/mdb.css';
import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import router from './router'
import VueApexCharts from 'vue-apexcharts'
import store from './store'

import Axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.prototype.$http = Axios;

Vue.use(VueApexCharts)
Vue.use(Vuex)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
