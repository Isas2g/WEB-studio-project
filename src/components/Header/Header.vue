<template>
  <header class="header">
    <div class="header__logo">Web-Studio</div>
    <ul class="header__nav">
      <li class="header__nav-item current">
        <router-link class="header__nav-link" to="/">Главная</router-link>
      </li>
      <li class="header__nav-item">
        <router-link class="header__nav-link" to="/blog">Блог</router-link>
      </li>
      <li class="header__nav-item">
        <router-link class="header__nav-link" to="/join"
          >Хочу вступить!</router-link
        >
      </li>
      <li class="header__nav-item">
        <router-link class="header__nav-link" to="/about">О нас</router-link>
      </li>
      <li class="header__nav-item">
        <router-link class="header__nav-link" to="/entry">Войти</router-link>
      </li>
    </ul>
  </header>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 30px 20px;

  .logo {
    font-size: 18px;
  }

  .current {
    font-weight: 800;
  }

  &__nav {
    display: flex;
    list-style: none;

    &-item {
      margin-right: 15px;
      cursor: pointer;
    }
    &-link {
      color: #fff;
      text-decoration: none;
    }
  }
}
</style>
