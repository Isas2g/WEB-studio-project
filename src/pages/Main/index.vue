<template>
  <main class="main container">
    <TitleBlock />

    <carousel-team>
      <carousel-slide />
    </carousel-team>

    <Projects :projects="projects" />

    <Feedback />

    <FooterForm />
    <Footer />
  </main>
</template>

<script>
import SmoothieFeed from "@/assets/images/smoothie-feed.jpg"
import CarouselTeam from "@/components/CarouselTeam"
import CarouselSlide from "@/components/CarouselSlide"
import Footer from "@/components/Footer"

import TitleBlock from './components/TitleBlock'
import Projects from './components/Projects'
import Feedback from './components/Feedback'
import FooterForm from './components/FooterForm'

import { mapActions, mapGetters } from 'vuex'

export default {
  components: { 
    CarouselSlide, 
    CarouselTeam, 
    TitleBlock, 
    Projects,
    Feedback,
    FooterForm,
    Footer
  },
  data: () => ({
    SmoothieFeed: SmoothieFeed,
    data: null
  }),
  computed: {
    ...mapGetters({
      projects: 'getProjects',
      users: 'getUsers'
    })
  },
  mounted() {
    this.loadProjects(),
    this.loadUsers()
  },
  methods: {
    ...mapActions({
      loadProjects: 'loadProjects',
      loadUsers: 'loadUsers'
    })
  }
};
</script>

<style lang="scss" scoped>

</style>