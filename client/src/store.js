import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.prototype.$http = axios;


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loggedIn: false,
    userID: -1

  },
  getters:{
    getLoggedIn(state){return '${state.loggedIn}'},
    getUserID(state){return '${state.userID}'}

  },
  mutations: {
    setLoggedIn(state){
      state.loggedIn = true
    },
    setUserID(state, id){
      state.userID = id
    },

  },
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {

        axios({ url: 'http://localhost:5000/login', data: user, method: 'POST' })
          .then(resp => {
            const token = resp.data.token
            const userID = resp.data.userID
            localStorage.setItem('token', token)
            if(userID != -1){
              commit('setLoggedIn')
              commit('setUserID', userID)
            }
            // Add the following line:
            //axios.defaults.headers.common['Authorization'] = token
            //commit('auth_success', token, user)
            resolve(resp)
          })
          .catch(err => {
            //commit('auth_error')
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },



  }



})
