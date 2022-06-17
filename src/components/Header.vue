<template>
  <header class="header">
    <nav class="menu-mobile container">
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
          <router-link class="header__nav-link" to="/">Мой профиль</router-link>
        </li>
        <li class="header__nav-item current">
          <router-link class="header__nav-link" to="/">Главная</router-link>
        </li>
        <li class="header__nav-item">
          <router-link class="header__nav-link" to="/tasks">Блог</router-link>
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
          <li class="header__nav-item mobile__link current">
            <svg
              width="30"
              height="30"
              viewBox="0 0 30 30"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M15 2.5C13.7639 2.5 12.5555 2.86656 11.5277 3.55331C10.4999 4.24007 9.6988 5.21619 9.22575 6.35823C8.75271 7.50027 8.62893 8.75693 8.87009 9.96931C9.11125 11.1817 9.7065 12.2953 10.5806 13.1694C11.4547 14.0435 12.5683 14.6388 13.7807 14.8799C14.9931 15.1211 16.2497 14.9973 17.3918 14.5242C18.5338 14.0512 19.5099 13.2501 20.1967 12.2223C20.8834 11.1945 21.25 9.98613 21.25 8.75C21.25 7.0924 20.5915 5.50269 19.4194 4.33058C18.2473 3.15848 16.6576 2.5 15 2.5ZM15 12.5C14.2583 12.5 13.5333 12.2801 12.9166 11.868C12.2999 11.456 11.8193 10.8703 11.5355 10.1851C11.2516 9.49984 11.1774 8.74584 11.3221 8.01841C11.4667 7.29098 11.8239 6.6228 12.3483 6.09835C12.8728 5.5739 13.541 5.21675 14.2684 5.07206C14.9958 4.92736 15.7498 5.00162 16.4351 5.28545C17.1203 5.56928 17.706 6.04993 18.118 6.66661C18.5301 7.2833 18.75 8.00832 18.75 8.75C18.75 9.74456 18.3549 10.6984 17.6517 11.4017C16.9484 12.1049 15.9946 12.5 15 12.5ZM26.25 26.25V25C26.25 22.6794 25.3281 20.4538 23.6872 18.8128C22.0462 17.1719 19.8206 16.25 17.5 16.25H12.5C10.1794 16.25 7.95376 17.1719 6.31282 18.8128C4.67187 20.4538 3.75 22.6794 3.75 25V26.25H6.25V25C6.25 23.3424 6.90848 21.7527 8.08058 20.5806C9.25269 19.4085 10.8424 18.75 12.5 18.75H17.5C19.1576 18.75 20.7473 19.4085 21.9194 20.5806C23.0915 21.7527 23.75 23.3424 23.75 25V26.25H26.25Z"
                fill="black"
              />
              <line
                x1="4"
                y1="26"
                x2="26"
                y2="26"
                stroke="black"
                stroke-width="2"
              />
            </svg>
            <router-link class="header__nav-link" to="/"
              >Мой профиль</router-link
            >
          </li>
          <li class="header__nav-item mobile__link">
            <svg
              width="23"
              height="24"
              viewBox="0 0 23 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M21.9167 20.8333V12.6812C21.9167 12.1141 21.801 11.5529 21.5766 11.032C21.3521 10.5111 21.0237 10.0416 20.6115 9.65208L12.9312 2.39374C12.5444 2.02804 12.0323 1.82428 11.5 1.82428C10.9677 1.82428 10.4556 2.02804 10.0687 2.39374L2.38854 9.65208C1.97627 10.0416 1.64786 10.5111 1.42343 11.032C1.199 11.5529 1.08327 12.1141 1.08333 12.6812V20.8333C1.08333 21.3859 1.30282 21.9158 1.69352 22.3065C2.08422 22.6972 2.61413 22.9167 3.16666 22.9167H19.8333C20.3859 22.9167 20.9158 22.6972 21.3065 22.3065C21.6972 21.9158 21.9167 21.3859 21.9167 20.8333Z"
                stroke="black"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
            <router-link class="header__nav-link" to="/">Главная</router-link>
          </li>
          <li class="header__nav-item mobile__link">
            <svg
              width="18"
              height="18"
              viewBox="0 0 18 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M0 15H7.5V16.5H0V15ZM0 10.5H7.5V12H0V10.5ZM16.5 7.5H1.5C1.10218 7.5 0.720644 7.34196 0.43934 7.06066C0.158035 6.77936 0 6.39782 0 6V1.5C0 1.10218 0.158035 0.720644 0.43934 0.43934C0.720644 0.158035 1.10218 0 1.5 0H16.5C16.8978 0 17.2794 0.158035 17.5607 0.43934C17.842 0.720644 18 1.10218 18 1.5V6C18 6.39782 17.842 6.77936 17.5607 7.06066C17.2794 7.34196 16.8978 7.5 16.5 7.5ZM1.5 1.5V6H16.5V1.5H1.5ZM16.5 18H12C11.6022 18 11.2206 17.842 10.9393 17.5607C10.658 17.2794 10.5 16.8978 10.5 16.5V12C10.5 11.6022 10.658 11.2206 10.9393 10.9393C11.2206 10.658 11.6022 10.5 12 10.5H16.5C16.8978 10.5 17.2794 10.658 17.5607 10.9393C17.842 11.2206 18 11.6022 18 12V16.5C18 16.8978 17.842 17.2794 17.5607 17.5607C17.2794 17.842 16.8978 18 16.5 18ZM12 12V16.5H16.5V12H12Z"
                fill="black"
              />
            </svg>
            <router-link class="header__nav-link" to="/blog">Блог</router-link>
          </li>
          <li class="header__nav-item mobile__link">
            <svg
              width="30"
              height="30"
              viewBox="0 0 30 30"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M9.375 15C9.37534 13.1763 9.90769 11.3923 10.9068 9.86662C11.9059 8.34095 13.3284 7.13989 15 6.41063C13.5732 5.78659 12.0135 5.52781 10.4616 5.65764C8.90975 5.78748 7.41468 6.30185 6.11143 7.15429C4.80818 8.00674 3.73781 9.17041 2.99699 10.5402C2.25617 11.91 1.86824 13.4427 1.86824 15C1.86824 16.5573 2.25617 18.09 2.99699 19.4598C3.73781 20.8296 4.80818 21.9933 6.11143 22.8457C7.41468 23.6982 8.90975 24.2125 10.4616 24.3424C12.0135 24.4722 13.5732 24.2134 15 23.5894C13.3284 22.8601 11.9059 21.6591 10.9068 20.1334C9.90769 18.6077 9.37534 16.8237 9.375 15Z"
                fill="black"
              />
              <path
                d="M15 8.50781C13.8598 9.16533 12.9129 10.1115 12.2546 11.2512C11.5962 12.3909 11.2496 13.6838 11.2496 15C11.2496 16.3162 11.5962 17.6091 12.2546 18.7488C12.9129 19.8885 13.8598 20.8347 15 21.4922C16.1402 20.8347 17.0871 19.8885 17.7454 18.7488C18.4038 17.6091 18.7504 16.3162 18.7504 15C18.7504 13.6838 18.4038 12.3909 17.7454 11.2512C17.0871 10.1115 16.1402 9.16533 15 8.50781Z"
                fill="black"
              />
              <path
                d="M18.75 5.625C17.4591 5.62469 16.1822 5.8922 15 6.41063C16.6718 7.13955 18.0946 8.34053 19.0938 9.86626C20.093 11.392 20.6253 13.1762 20.6253 15C20.6253 16.8238 20.093 18.608 19.0938 20.1337C18.0946 21.6595 16.6718 22.8604 15 23.5894C16.2772 24.1473 17.6628 24.4133 19.0558 24.3682C20.4488 24.3231 21.8142 23.9679 23.0526 23.3285C24.2911 22.6891 25.3713 21.7816 26.2148 20.6721C27.0583 19.5626 27.6437 18.2789 27.9285 16.9146C28.2133 15.5502 28.1903 14.1396 27.8612 12.7852C27.532 11.4309 26.905 10.167 26.0258 9.08561C25.1466 8.00418 24.0373 7.13241 22.7787 6.53376C21.52 5.93512 20.1437 5.62466 18.75 5.625Z"
                fill="black"
              />
            </svg>
            <router-link class="header__nav-link" to="/join"
              >Хочу вступить!</router-link
            >
          </li>
          <li class="header__nav-item mobile__link">
            <!-- <img :src="aboutUs" alt="" /> -->
            <router-link class="header__nav-link" to="/about"
              >О нас</router-link
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
// import aboutUs from "@/assets/images/burger-about-us.png";

export default {
  data: () => ({
    logoWeb: logoWeb,
  }),
  methods: {
    burgerMenuOpen() {
      const burgerMenu = document.querySelector(".mobile__menu-burger");
      const body = document.querySelector("body");
      body.classList.add("fixed");
      burgerMenu.classList.add("is-show");
    },
    burgerMenuClose() {
      const burgerMenu = document.querySelector(".mobile__menu-burger");
      const body = document.querySelector("body");
      body.classList.remove("fixed");
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
    &__link {
      display: flex;
      align-items: center;
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
    &__nav-link {
      padding: 0 0 0 10px;
    }
  }
}

@media screen and (max-width: 264px) {
  .logo {
    max-width: 60px;
  }
}
</style>
