import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    projects: [],
    users: []
  },
  actions: {
    loadProjects (ctx) {
      axios
      .get('/projects/')
      .then(data => {
        this.data = data;
        // console.log(this.data.data);
        ctx.commit('SET_projects', this.data.data.results)
      });
    },
    loadUsers (ctx) {
      axios
      .get('/users/')
      .then(data => {
        this.data = data
        ctx.commit('SET_users', this.data.data.results)
      })
    }
  },
  mutations: {
    SET_projects (state, projects) {
      state.projects = projects
    },
    SET_users (state, users) {
      state.users = users
    }
  },
  getters: {
    getProjects (state) {
      return state.projects
    },
    getUsers (state) {
      return state.users
    }
  }
})
