<template>
  <div class="container">
    <main class="main">
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
    </main>
    <footer class="footer">
      <section class="footer__block">
        <h1 class="footer__title title">Связаться с нами</h1>
        <div class="footer__form">
          <form class="footer__form name">
            <input type="text" id="name" name="name" />
          </form>
        </div>
      </section>
    </footer>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
.main {
  &__block {
    padding: 150px 0 150px 0;
  }
}

.footer {
  &__block {
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  &__form {
  }
}
</style>