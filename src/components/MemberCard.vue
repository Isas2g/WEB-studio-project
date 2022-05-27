<template>
  <li class="direction__member member">
    <img
      class="direction__member-image member__image"
      :src="image"
      :alt="name"
    />
    <h4 class="direction__mamber-name member__name">{{ name }}</h4>
    <h5 class="direction__mamber-description member__description">
      {{ description }}
    </h5>
  </li>
</template>

<script>
export default {
  props: {
    name: String,
    description: String,
    image: String,
  },
};
</script>

<style lang="scss">
.member {
  flex-basis: 20%;
  &__image {
    width: 100%;
    border-radius: 50%;
  }

  &__name {
    text-align: center;
  }
  &__description {
    text-align: center;
  }
}

@media (max-width: 768px) {
  .member {
    &__image {
      width: 150px;
      display: block;
      margin: 0 auto;
    }
  }
}
</style>