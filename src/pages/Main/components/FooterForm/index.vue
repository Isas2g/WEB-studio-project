<template>
  <section class="footer container">
    <div class="footer__body">
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
    </div>
  </section>
</template>

<script>

  export default {
    name: 'FooterForm'
  }

</script>

<style lang="scss" scoped>
  .footer {
    &__body {
      color: white;
      align-content: end;
      justify-content: center;
      margin-top: 291px;
      text-align: center;
      width: 100%;
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
  @media (max-width: 768px) {
    .footer {
      &__body {
        color: white;
        justify-items: center;
        margin-left: 4%;
        text-align: center;
        width: 98%;
      }

      &__subtitle {
        text-align: center;
        font-size: 16px;
      }

      &__title {
        text-align: center;
        font-size: 30px;
      }

      &__form {
        padding-top: 78px;
        padding-bottom: 89px;
        display: grid;
        grid-row-gap: 60px;
        grid-column-gap: 80px;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-areas:
          "name name name"
          "phone phone phone"
          "email email email"
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
  }
  @media screen and (max-width: 376px) {
    .footer {
      &__body {
        color: white;
        justify-items: center;
        padding: 0 42px 0 42px;
        margin-left: 0;
        text-align: center;
        width: 100%;
      }

      &__subtitle {
        text-align: center;
        font-size: 16px;
      }

      &__title {
        text-align: center;
        font-size: 30px;
      }

      &__form {
        padding-top: 78px;
        padding-bottom: 89px;
        display: grid;
        grid-row-gap: 60px;
        grid-column-gap: 80px;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-areas:
          "name name name"
          "phone phone phone"
          "email email email"
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
      .more-btn
      {
        max-width: 200px;
        margin-bottom: 80px;
      }
    }
  }
</style>