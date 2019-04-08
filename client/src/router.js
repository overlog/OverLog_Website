import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import BoxPlot from './components/BoxPlot'
import Developers from './components/Developers.vue'
import Login from './components/Login.vue'
import Register from './components/Register.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/boxplot',
      name: 'boxplot',
      component: BoxPlot
    },
    {
      path: '/developers',
      name: 'develoers',
      component: Developers
    },
    {
      path: '/login',
      name: 'login',
      component: Login  
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
  ]
})
