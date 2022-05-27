<template>
  <li class="feedback__review review">
    <div class="review__person-info">
      <img class="review__person-image" :src="image" alt="" />
      <h4 class="review__person-name">{{ name }}</h4>
    </div>
    <div class="review__content">
      <h5 class="review__text">
        {{ text }}
      </h5>
      <div class="review__stars">
        <svg
          class="review__star"
          width="36"
          height="32"
          viewBox="0 0 36 32"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M18 0L22.0413 12.0922L35.119 12.0922L24.5389 19.5656L28.5801 31.6578L18 24.1844L7.41987 31.6578L11.4611 19.5656L0.880983 12.0922L13.9587 12.0922L18 0Z"
            fill="url(#paint0_linear_662_154)"
          />
          <defs>
            <linearGradient
              id="paint0_linear_662_154"
              x1="-5.31325"
              y1="-10.4054"
              x2="22.3581"
              y2="-7.57278"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#FF0000" />
              <stop offset="1" stop-color="#FF008A" />
            </linearGradient>
          </defs>
        </svg>

        <svg
          class="review__star"
          width="36"
          height="32"
          viewBox="0 0 36 32"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M18 0L22.0413 12.0922L35.119 12.0922L24.5389 19.5656L28.5801 31.6578L18 24.1844L7.41987 31.6578L11.4611 19.5656L0.880983 12.0922L13.9587 12.0922L18 0Z"
            fill="url(#paint0_linear_662_154)"
          />
          <defs>
            <linearGradient
              id="paint0_linear_662_154"
              x1="-5.31325"
              y1="-10.4054"
              x2="22.3581"
              y2="-7.57278"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#FF0000" />
              <stop offset="1" stop-color="#FF008A" />
            </linearGradient>
          </defs>
        </svg>

        <svg
          class="review__star"
          width="36"
          height="32"
          viewBox="0 0 36 32"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M18 0L22.0413 12.0922L35.119 12.0922L24.5389 19.5656L28.5801 31.6578L18 24.1844L7.41987 31.6578L11.4611 19.5656L0.880983 12.0922L13.9587 12.0922L18 0Z"
            fill="url(#paint0_linear_662_154)"
          />
          <defs>
            <linearGradient
              id="paint0_linear_662_154"
              x1="-5.31325"
              y1="-10.4054"
              x2="22.3581"
              y2="-7.57278"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#FF0000" />
              <stop offset="1" stop-color="#FF008A" />
            </linearGradient>
          </defs>
        </svg>

        <svg
          class="review__star"
          width="36"
          height="32"
          viewBox="0 0 36 32"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M18 0L22.0413 12.0922L35.119 12.0922L24.5389 19.5656L28.5801 31.6578L18 24.1844L7.41987 31.6578L11.4611 19.5656L0.880983 12.0922L13.9587 12.0922L18 0Z"
            fill="url(#paint0_linear_662_154)"
          />
          <defs>
            <linearGradient
              id="paint0_linear_662_154"
              x1="-5.31325"
              y1="-10.4054"
              x2="22.3581"
              y2="-7.57278"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#FF0000" />
              <stop offset="1" stop-color="#FF008A" />
            </linearGradient>
          </defs>
        </svg>

        <svg
          class="review__star"
          width="36"
          height="32"
          viewBox="0 0 36 32"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M18 0L22.0413 12.0922L35.119 12.0922L24.5389 19.5656L28.5801 31.6578L18 24.1844L7.41987 31.6578L11.4611 19.5656L0.880983 12.0922L13.9587 12.0922L18 0Z"
            fill="url(#paint0_linear_662_154)"
          />
          <defs>
            <linearGradient
              id="paint0_linear_662_154"
              x1="-5.31325"
              y1="-10.4054"
              x2="22.3581"
              y2="-7.57278"
              gradientUnits="userSpaceOnUse"
            >
              <stop stop-color="#FF0000" />
              <stop offset="1" stop-color="#FF008A" />
            </linearGradient>
          </defs>
        </svg>
      </div>
    </div>
  </li>
</template>

<script>
import defaultPicture from "../../../assets/images/user-icon.png";

export default {
  data: () => ({
    defaultPicture: defaultPicture,
  }),
  props: {
    name: String,
    text: String,
    image: String,
    stars: Number,
  },
};
</script>

<style scoped lang="scss">
.test path {
  fill: white;
}
.review {
  display: flex;
  margin: 30px 0 0 0;

  &__person-info {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  &__person-name {
    margin: 10px 0 0 0;
  }

  &__content {
    margin: 10px 0 0 50px;
  }

  &__stars {
    margin: 10px 0 0 0;
  }
}
</style>