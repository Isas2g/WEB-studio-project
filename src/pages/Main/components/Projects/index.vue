<template>
  <section class="projects">
    
  </section>
</template>

<script>
import BtnLeftArr from "@/assets/images/btn-left-strelka.png";
import BtnArr from "@/assets/images/btn-strelka.png";

export default {
  name: 'Projects',
  props: {
    projects: Array
  },
  data: () => ({
    BtnArr: BtnArr,
    BtnLeftArr: BtnLeftArr,
    slideCount: 1
  }),
  methods: {

  },
}

</script>

<style scoped lang="scss">
.team__body {
  margin-bottom: 40px;
}


.carousel {
  overflow: hidden;
  position: relative;
  height: 370px;
}

.carousel-track {
    display: flex;
    top: 0;
    position: absolute;
    left: 0%;
    transition: 0.3s;
  }
  .carousel-track.management {
    left: 0%;
  }
  .carousel-track.backend {
    left: -100%;
  }
  .carousel-track.frontend {
    left: -200%;
  }
  .carousel-track.design {
    left: -300%;
  }

.carousel-item.item {
  flex-shrink: 0;
  min-width: 36%;
  padding-left: 50px;
  padding-right: 50px;
}

.carousel-btn {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 2;
  display: flex;
  justify-content: space-between;
}
.btn-prev, .btn-next {
  background: none;
  border: none;
  outline: none;
  cursor: pointer;
}

.item {
  .member {
    width: 240px;
    flex-basis: unset;
    margin-left: 15px;
    margin-right: 15px;
  }

  &__members {
    display: flex;
    justify-content: space-between;
  }

  .members-two {
    justify-content: center;

    .item__member:first-of-type {
      margin: 0 30px 0 0;
    }

    .item__member:not(:first-of-type) {
      margin: 0 0 0 30px;
    }
  }
}

.team {
  &__title {
    margin-bottom: 20px;
  }
}
</style>