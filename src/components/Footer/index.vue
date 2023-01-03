<template>
  <main class="footer">
    <div class="footer__column">
      <img class="footer__logo" :src="logoWeb" alt="logo"/>
      <p class="footer__text">
        +7 (999) 999-99-99
      </p>
      <p class="footer__text">
        группа Вконтакте
      </p>
      <p class="footer__text">
        telegram
      </p>
      <p class="footer__text">
        about_web@info.ru
      </p>
    </div>
    <div class="footer__column">
      <h3 class="footer__title">
        Обсудим проект?
      </h3>
      <form class="footer__form form" id="project">
        <input
            class="form__input name"
            type="text"
            id="name"
            name="name"
            placeholder="ИМЯ"
        />
        <input
            class="form__input surname"
            type="text"
            id="surname"
            name="surname"
            placeholder="ФАМИЛИЯ"
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
            placeholder="ПАРА СЛОВ О ПРОЕКТЕ"
        />
      </form>
      <div class="footer__checkbox">
        <input class="footer__checkbox-btn" type="checkbox" id="agreed" name="agreed"/>
        <label for="agreed">Я ознакомился и соглашаюсь с политикой конфиденциальности</label>
      </div>
      <button class="footer__more-btn more-btn" form="project">Отправить</button>
    </div>
  </main>
</template>

<script>
import logoWeb from "@/assets/images/logo-web.png";

export default {
  name: "index",
  data: () => ({
    logoWeb: logoWeb,
  }),
}
</script>

<style lang="scss" scoped>

.footer {
  margin: 50px 0 0 0;
  display: flex;
  flex-direction: row;
  column-gap: 200px;

  &__column {
    display: flex;
    flex-direction: column;
  }

  &__logo {
    font-size: 18px;
    max-width: 100px;
    margin: 0 0 0 -10px;
  }

  &__title {
    margin: 15px 0 0 0;
    text-align: start;
  }

  &__form {
    padding-top: 50px;
    padding-bottom: 50px;
    display: grid;
    grid-row-gap: 60px;
    grid-column-gap: 80px;
    grid-template-columns: 1fr 1fr;
    grid-template-areas:
        "name sur"
        "phone email"
        "com com";
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

  .surname {
    grid-area: sur;
    width: 100%;
    background: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    color: white;
    height: 25px;
  }

  &__more-btn {
    margin: 20px 0 20px 0;
    max-width: 200px;
  }
  
  &__checkbox {
    margin: 0 0 20px 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
}

</style>