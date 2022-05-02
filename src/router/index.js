import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from "../pages/Main/MainPage.vue";
import AboutPage from "../pages/About/AboutPage.vue";
import JoinPage from "../pages/Join/JoinPage.vue";
import FeedbackPage from "@/pages/Feedback/FeedbackPage";


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'MainPage',
        component: MainPage
    },
    {
        path: '/about',
        name: 'ApoutPage',
        component: AboutPage
    },
    {
        path: '/join',
        name: 'JoinPage',
        component: JoinPage
    },
    {
        path: '/feedback',
        name: 'FeedbackPage',
        component: FeedbackPage
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
