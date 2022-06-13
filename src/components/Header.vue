<template>
  <header class="header">
    <nav class="menu-mobile">
      <img :src="logoWeb" alt="" />
      <div class="burger-menu-button" @click="burgerMenuOpen">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="35"
          height="20"
          viewBox="0 0 35 20"
          fill="none"
        >
          <rect x="5" width="30" height="2" rx="1" fill="#f2ddde"></rect>
          <rect y="9" width="30" height="2" rx="1" fill="#f2ddde"></rect>
          <rect
            x="10"
            y="18"
            width="25"
            height="2"
            rx="1"
            fill="#f2ddde"
          ></rect>
        </svg>
      </div>
    </nav>

    <nav class="header__menu menu-desktop">
      <img class="header__logo" :src="logoWeb" alt="Logo" />
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
    </nav>

    <div class="mobile__menu-burger">
      <div class="mobile__menu-content">
        <div class="mobile__profile">
          <svg
            class="mobile__profile-picture"
            width="68"
            height="68"
            viewBox="0 0 68 68"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle cx="34" cy="34" r="34" fill="black" />
            <path
              d="M33.9032 35.2871C20.7743 35.2871 16 53.7698 16 53.7698H22.5644H45.2418H53C53 53.7698 47.0322 35.2871 33.9032 35.2871Z"
              fill="white"
            />
            <ellipse
              cx="33.765"
              cy="23.5898"
              rx="8.76498"
              ry="9"
              fill="white"
            />
          </svg>

          <div class="mobile__profile-info">
            <h4 class="mobile__profile-name">Имя</h4>
            <h4 class="mobile__profile-position">Должность</h4>
          </div>
        </div>
        <hr class="mobile__line" />
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
            <router-link class="header__nav-link" to="/about"
              >О нас</router-link
            >
          </li>
          <li class="header__nav-item">
            <router-link class="header__nav-link" to="/entry"
              >Войти</router-link
            >
          </li>
        </ul>
        <h5 class="mobile__exit">Выйти</h5>
        <hr class="mobile__line mobile__line--bottom" />
        <div class="mobile-cross" @click="burgerMenuClose">
          <svg
            width="23"
            height="21"
            viewBox="0 0 23 21"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <line
              x1="3.53553"
              y1="2.5"
              x2="18.3848"
              y2="17.3492"
              stroke="black"
              stroke-width="5"
              stroke-linecap="round"
            />
            <line
              x1="3.62755"
              y1="17.4645"
              x2="18.4768"
              y2="2.61522"
              stroke="black"
              stroke-width="5"
              stroke-linecap="round"
            />
          </svg>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import logoWeb from "@/assets/images/logo-web.png";

export default {
  data: () => ({
    logoWeb: logoWeb,
  }),
  methods: {
    burgerMenuOpen() {
      const burgerMenu = document.querySelector(".mobile__menu-burger");
      burgerMenu.classList.add("is-show");
    },
    burgerMenuClose() {
      const burgerMenu = document.querySelector(".mobile__menu-burger");
      burgerMenu.classList.remove("is-show");
    },
  },
};
</script>

<style lang="scss" scoped>
.header {
  &__menu {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 30px 65px 20px 65px;
  }

  .logo {
    font-size: 18px;
    max-width: 80px;
  }

  .current {
    font-weight: 800;
  }

  &__nav {
    display: flex;

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

@media (min-width: 768px) {
  .menu-mobile {
    display: none;
  }
  .mobile__menu-burger {
    display: none;
  }
}
@media (max-width: 767.5px) {
  .menu-desktop {
    display: none;
  }
  .menu-mobile {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .mobile__menu-burger {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.774);
    z-index: 30;
    transform: translate(-100%, 0);
    transition: all ease 0.3s;
  }
  .is-show {
    transform: translate(0);
  }
  .mobile__menu-content {
    background-image: linear-gradient(120deg, #f70193, #a72cf2);
    width: 250px;
    height: 100%;
    position: relative;
    color: black;
  }
  .mobile-cross {
    position: absolute;
    top: 10px;
    right: 10px;
  }

  .mobile {
    &__profile {
      display: flex;
      align-items: center;
      padding: 10px;
    }
    &__profile-info {
      margin: 0 0 0 10px;
    }
    &__line {
      background-color: black;
      border: 0.5px solid black;

      &--bottom {
        position: absolute;
        bottom: 30px;
        width: 100%;
      }
    }
    &__exit {
      position: absolute;
      bottom: 10px;
      right: 10px;
    }
  }
  .header {
    &__nav {
      display: flex;
      flex-direction: column;
      a {
        color: black;
      }
    }
  }
}

@media screen and (max-width: 264px) {
  .logo {
    max-width: 60px;
  }
}
</style>
