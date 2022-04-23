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
      <section class="footer__body">
        <h1 class="footer__title title">Связаться с нами</h1>
        <p class="footer__subtitle subtitle">
          Оставьте свои контакты и мы свяжемся с вами в ближайшее время
        </p>
        <form class="footer__form" id="form">
          <input
            class="name"
            type="text"
            id="name"
            name="name"
            placeholder="ИМЯ"
          />
          <input
            class="phone"
            type="text"
            id="phone"
            name="phone"
            placeholder="ТЕЛЕФОН"
          />
          <input
            class="email"
            type="text"
            id="email"
            name="email"
            placeholder="EMAIL"
          />
          <input
            class="com"
            type="text"
            id="com"
            name="com"
            placeholder="КОММЕНТАРИЙ"
          />
        </form>
        <button class="footer__more-btn more-btn" form="form">Связаться</button>
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
  &__body {
    color: white;
    align-content: end;
    justify-content: center;
  }
  &__form {
    padding-bottom: 89px;
    display: grid;
    grid-row-gap: 60px;
    grid-column-gap: 80px;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-areas:
      "name phone email"
      "com com com";
  }
  .name {
    grid-area: name;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    color: white;
    height: 25px;
  }
  .phone {
    grid-area: phone;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    color: white;
    height: 25px;
  }
  .email {
    grid-area: email;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    color: white;
    height: 25px;
  }
  .com {
    grid-area: com;
    width: 100%;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    color: white;
    height: 25px;
  }
}
</style>