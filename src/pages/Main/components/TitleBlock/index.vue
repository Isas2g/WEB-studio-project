<template>
  <section class="main__block">
    <h1 class="main__title title">
      Студенческая веб-студия Московского Политеха
    </h1>
    <p class="main__subtitle subtitle">
      Мы крутые ребята из Московского политеха и создаем крутой контент для
      тебя и всех остальных
    </p>
    <button class="main__more-btn more-btn">Подробнее</button>
  </section>
</template>

<script>

export default {
  name: 'TitleBlock'
}
</script>

<style scoped lang="scss">
  .main {
    &__block {
      max-width: 800px;
      padding: 0 0 150px 0;
    }
    &__title {
      text-align: start;
      margin-bottom: 20px;
    }
    &__subtitle {
      max-width: 440px;
      margin-bottom: 73px;
    }
  }

  @media (max-width: 768px) {
    .main {
      &__block {
        margin-left: 5%;
        margin-right: 10%;
      }
      &__title {
        text-align: start;
        margin-bottom: 20px;
        font-size: 30px;
      }
      &__subtitle {
        margin-bottom: 73px;
        font-size: 16px;
      }
    }
  }
  @media screen and (max-width: 376px) {
    .main {
      &__block {
        width: auto;
        margin-left: 5%;
      }
    }
  }
</style>

