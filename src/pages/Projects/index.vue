<template>
  <div>
    <main class="projects container">
      <section class="project__body">
        <h1 class="project__title">Наши проекты</h1>
        <img :src="$route.params.project.icon" alt="" class="project__image">
        <h4 class="project__title-project">{{ $route.params.project.title }}</h4>
        <p class="project__description">{{ $route.params.project.description }}</p>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: "OurProjects",
  data: () => ({
    // project: this.$route.params.project
  })
}
</script>

<style scoped lang="scss">
  .project {
    &__body {
      display: flex;
      align-items: center;
      flex-direction: column;
    }
  }
  .project {
    &__image {
      border-radius: 15px;
      max-width: 30%;
      height: auto;
      margin: 30px 0 0 0;
    }
    &__title-project {
      font-weight: 600;
      font-size: 35px;
      line-height: 42px;
      margin: 30px 0 0 0;
    }

    &__description {
      font-weight: 400;
      font-size: 16px;
      line-height: 32px;
      margin: 30px 0 0 0;
    }
  }
</style>