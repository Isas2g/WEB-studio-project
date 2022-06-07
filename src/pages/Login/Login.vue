<template>
  <main class="main container">
    <h1 class="main__title title">Вход</h1>
    <section class="main block">
      <form class="main__form form" id="form">
        <input
            class="form__input name"
            type="text"
            id="name"
            name="name"
            placeholder="Ваш логин"
        />
        <input
            class="form__input password"
            type="text"
            id="password"
            name="password"
            placeholder="Ваш пароль"
        />
      </form>
      <button class="main__more-btn more-btn" form="form">Вход</button>
      <p class="main__check-btn text"><input class="main__check-btn check-btn" type="checkbox" name="remember" value="Запомнить меня"><label for="">Запомнить меня</label></p>
      <router-link class="main__forgotten forgotten" to="/recovery"
      >Забыли логин или пароль?
      </router-link
      >
    </section>
  </main>
</template>

<script>
export default {
  name: "Login"
}
</script>

<style scoped lang="scss">
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title {
  margin-bottom: 3%;
}
.block {
  background: linear-gradient(95.68deg, #FF008A -16.11%, #8002FF 54.53%);
  border-radius: 10px;
  width: 50%;
  display: grid;
  grid-row-gap: 5px;
  grid-column-gap: 1px;
  grid-template-columns: 2fr 1fr 2fr;
  grid-template-areas:
      "name name name"
      "password password password"
      "text . forgotten"
      ". login .";
}
.form {
  border-radius: 5px;
  margin-top: 5%;
  margin-left: 5%;
}

.form__input {
  border-radius: 10px;
  width: 100%;
  border: none;
  font-size: 16px;
  margin: 5%;
  padding-left: 5%;
}

.name {
  grid-area: name;
  height: 47px;
}

.password {
  grid-area: password;
  height: 47px;
}
.more-btn {
  grid-area: login;
  margin-bottom: 15%;
}
.check-btn {
  height: 24px;
  width: 24px;
  margin-left: 10%;
  margin-right: 5%;
}
.forgotten {
  grid-area: forgotten;
  margin-right: 2%;
  text-decoration: underline;
}
.text {
  grid-area: text;
  display: flex;
  align-items: center;
}

input[type="text"] {
  background: #ffffff;
  color: linear-gradient(95.68deg, #FF008A -16.11%, #8002FF 54.53%);
}
</style>