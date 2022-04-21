import Vue from 'vue'
import VueRouter from 'vue-router'
// import MainPage from "../pages/MainPage";


Vue.use(VueRouter)

const routes = [
    // {
    //     path: '/main',
    //     name: 'MainPage',
    //     component: MainPage
    // },

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
