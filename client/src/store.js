import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loggingIn: false,
    loginError: null,
    loginSuccessfull: false
  },
  mutations: {
    loginStart: state => state.loggingIn = true,
    loginStop: (state, errorMessage) => {
      state.loggingIn = false;
      state.loginError = errorMessage;
      state.loginSuccessfull = !errorMessage;
    }
  },
  actions: {
    Login({commit}, loginData) {
      commit('loginStart');

      Axios.post('https://reqres.in/api/login', {
      ...loginData
      })
      .then(() => {
        commit('loginStop', null)
      })
      .catch(error => {
        commit('loginStop', error.response.data.error)
      })
    }
  }
})
