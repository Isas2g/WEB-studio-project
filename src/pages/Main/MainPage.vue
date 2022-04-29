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
    <feedback class="feedback">
      <section class="feedback__body">
        <section class="feedback__first-column">
          <h1 class="feedback__title title">Отзывы</h1>
          <p class="feedback__subtitle subtitle">Почитайте отзывы...</p>
          <button class="feedback__more-btn more-btn">Все отзывы</button>
        </section>
        <section class="feedback__space"></section>
        <section class="feedback__second-column">
          <img
              class="feedback__user-icon"
              src="../../assets/images/user-icon.png"
              alt="Юзер"
          />
          <p class="feedback__text name">Александр</p>
          <p class="feedback__text text">Быстро и качественно сделали сайт! Рекомендую!</p>
        </section>
      </section>
    </feedback>
    <footer class="footer">
      <section class="footer__body">
        <h1 class="footer__title title">Связаться с нами</h1>
        <p class="footer__subtitle subtitle">
          Оставьте свои контакты и мы свяжемся с вами в ближайшее время
        </p>
        <form class="footer__form" id="form">
          <input
            class="form__input name"
            type="text"
            id="name"
            name="name"
            placeholder="ИМЯ"
          />
          <input
            class="form__input phone"
            type="text"
            id="phone"
            name="phone"
            placeholder="ТЕЛЕФОН"
          />
          <input
            class="form__input email"
            type="text"
            id="email"
            name="email"
            placeholder="EMAIL"
          />
          <input
            class="form__input com"
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
    max-width: 800px;
    padding: 150px 0 150px 0;
  }
  &__title {
    text-align: start;
  }
  &__subtitle {
    max-width: 440px;
  }
}

.feedback {
  &__body {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0 150px 330px 150px;
  }

  .name {
    font-weight: bold;
  }

  &__first-column {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  &__second-column {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  &__user-icon {
    max-width: 146px;
  }
}

.footer {
  &__body {
    color: white;
    align-content: end;
    justify-content: center;
    padding: 0 150px 0 150px;
    text-align: center;
  }

  &__subtitle {
    text-align: center;
  }

  &__title {
    text-align: center;
  }

  &__form {
    padding-top: 78px;
    padding-bottom: 89px;
    display: grid;
    grid-row-gap: 60px;
    grid-column-gap: 80px;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-areas:
      "name phone email"
      "com com com";
  }
  .form__input {
    width: 100%;
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