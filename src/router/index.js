import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from "../pages/Main/";
import AboutPage from "../pages/About/";
import JoinPage from "../pages/Join/";
import OurProjects from "@/pages/Projects/";
import FeedbackPage from "../pages/Feedback/";
import WorkInProgress from "../components/WorkInProgress/";
import LoginPage from "@/pages/Login/";
import Profile from "@/pages/Profile/";
import Tasks from "@/pages/Tasks/";


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
        path: '/ourprojects/:project',
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
        component: LoginPage
    },
    {
        path: '/recovery',
        name: 'WorkInProgress',
        component: WorkInProgress
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile
    },
    {
        path: '/tasks',
        name: 'Tasks',
        component: Tasks
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
