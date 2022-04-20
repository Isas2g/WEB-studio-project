<template>
  <div class="container">
    <header>
      <div class="logo">
        Web-Studio
      </div>
      <ul>
        <li class="current">Главная</li>
        <li>Блог</li>
        <li>Хочу вступить!</li>
        <li>О нас</li>
        <li>Войти</li>
      </ul>
    </header>

    <main>
      <section>
        <h1>Студенческая веб-студия Московского Политеха</h1>
        <p>Мы крутые ребята из Московского политеха и создаем крутой контент для тебя и всех остальных</p>
        <button>Подробнее</button>
      </section>
    </main>

  </div>
</template>

<script>
  export default {
    name: 'MainPage',
    // ...
  };
</script>

<style lang="scss">
  body {
    background: #000;
    color: #fff;
  }

  .container {
    max-width: 1200px;
    padding: 15px;
    margin: 0 auto;
    font-family: 'inter';
  }

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    .logo {
      font-size: 18px;
    }

    .current {
      font-weight: 800;
    }

    ul {
      display: flex;
      list-style: none;

      li {
        margin-right: 15px;
        cursor: pointer;
      }
    }
  }

</style>