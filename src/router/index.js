import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from "../pages/Main/MainPage.vue";
import AboutPage from "../pages/About/AboutPage.vue";
import JoinPage from "../pages/Join/JoinPage.vue";
import OurProjects from "@/pages/Projects/OurProjects";
import FeedbackPage from "../pages/Feedback/FeedbackPage";
import WorkInProgress from "../components/WorkInProgress";
import Login from "@/pages/Login/Login";


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
    {
        path: '/ourprojects',
        name: 'OurProjects',
        component: OurProjects
    },
    {
        path: '/blog',
        name: 'WorkInProgress',
        component: WorkInProgress
    },
    {
        path: '/entry',
        name: 'Login',
        component: Login
    },
    {
        path: '/recovery',
        name: 'WorkInProgress',
        component: WorkInProgress
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
