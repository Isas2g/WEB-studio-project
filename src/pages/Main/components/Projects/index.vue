<template>
  <section class="projects">
    <h1 class="projects__title">Наши проекты</h1>
    <ul class="projects__list">
      <li class="projects__project project" v-for="(project, index) in projects" :key="index">
        <img class="project__image" :src="project.icon" alt="">
        <h4 class="project__title">{{ project.title }}</h4>
        <!-- <button class="project__button more-btn" >Подробнее</button> -->
        <router-link class="project__button more-btn" type="button" :to="{ name: 'OurProjects', params: {project: project}}">Подробнее</router-link>
      </li>
    </ul>
    <img class="projects__left-arrow" v-on:click="rollSlider('left')" :src="BtnLeftArr" alt="">
    <img class="projects__right-arrow" v-on:click="rollSlider('right')" :src="BtnArr" alt="">
  </section>
</template>

<script>
import BtnLeftArr from "@/assets/images/btn-left-strelka.png";
import BtnArr from "@/assets/images/btn-strelka.png";

export default {
  name: 'Projects',
  props: {
    projects: Array
  },
  data: () => ({
    BtnArr: BtnArr,
    BtnLeftArr: BtnLeftArr,
    sliderCount: 0,
  }),
  computed: {

  },
  methods: {
    rollSlider (direction) {
      const slider = document.querySelector('.projects__list')
      const slides = document.querySelectorAll('.project')

      if (this.sliderCount + 1 <= slides.length && direction === 'right') {
        this.sliderCount++
        slider.style.transform = "translateX(" + -100 * this.sliderCount + "%)"
        
        if (this.sliderCount === slides.length) {
          this.sliderCount = 0
          slider.style.transform = "translateX(0%)"
        }
      }

      if (this.sliderCount > 0 && direction === 'left') {
        this.sliderCount--
        slider.style.transform = "translateX(" + -100 * this.sliderCount + "%)"

      } else if (this.sliderCount === 0 && direction === 'left') {
        this.sliderCount = slides.length - 1
        slider.style.transform = "translateX(" + -100 * this.sliderCount + "%)"
      }
    }
  }
}

</script>

<style scoped lang="scss">

  .projects {
    overflow: hidden;
    position: relative;

    &__list {
      display: flex;
      position: relative;
      transition: 400ms;
      margin: 30px 0 0 0;
    }
    &__left-arrow {
      position: absolute;
      left: 0;
      top: 50%;
      margin-top: -30px;
      pointer-events: auto;
      cursor: pointer;
    }
    &__right-arrow {
      position: absolute;
      right: 0;
      top: 50%;
      margin-top: -30px;
      pointer-events: auto;
      cursor: pointer;
    }
  }
  .project {
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
    min-width: 100%;
    
    &__image {
      display: block;
      width: 350px;
      border-radius: 15px;
    }
    &__title {
      font-family: 'Inter';
      font-style: normal;
      font-weight: 600;
      font-size: 30px;
      line-height: 42px;
      text-align: center;
      margin: 30px 0 0 0;

      color: #FFFFFF;
    }
    &__button {
      margin: 30px 0 0 0;
      background: linear-gradient(95.68deg, #FF0000 -16.11%, #FF008A 54.53%);
      border-radius: 5px;
    }
  }
</style>