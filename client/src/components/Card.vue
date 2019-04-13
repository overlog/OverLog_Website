<template>
  <flipper
    class="Card"
    width="270px"
    height="300px"
    :flipped="isFlipped"
    @click="isFlipped = !isFlipped"
  >
    <div class="Card__face" slot="front">
      <span class="Card__value Card__value--top">10</span>
      <span class="Card__center">♣</span>
      <span class="Card__value Card__value--bottom">10</span>
    </div>

    <figure class="Card__pattern" slot="back"></figure>
  </flipper>
</template>

<script>
import Flipper from "vue-flipper";

export default {
  components: { Flipper },
  data: () => ({ isFlipped: false })
};
</script>

<style src="vue-flipper/dist/vue-flipper.css" />

<style lang="stylus">
.Card {
  &__face, &__pattern {
    width: 100%;
    height: @width;
    border-radius: 20px;
    box-shadow: 0 3px 15px rgba(#000, 0.45);
    cursor: pointer;
  }

  &__pattern {
    background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iNjAiIGhlaWdodD0iMzAiPgo8ZGVmcz4KPHJlY3QgaWQ9InIiIHdpZHRoPSIzMCIgaGVpZ2h0PSIxNSIgZmlsbD0iI2JiMDg1ZiIgc3Ryb2tlLXdpZHRoPSIyLjUiIHN0cm9rZT0iIzdhMDU0ZCI+PC9yZWN0Pgo8ZyBpZD0icCI+Cjx1c2UgeGxpbms6aHJlZj0iI3IiPjwvdXNlPgo8dXNlIHk9IjE1IiB4bGluazpocmVmPSIjciI+PC91c2U+Cjx1c2UgeT0iMzAiIHhsaW5rOmhyZWY9IiNyIj48L3VzZT4KPHVzZSB5PSI0NSIgeGxpbms6aHJlZj0iI3IiPjwvdXNlPgo8L2c+CjwvZGVmcz4KPHVzZSB4bGluazpocmVmPSIjcCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCAtMjUpIHNrZXdZKDQwKSI+PC91c2U+Cjx1c2UgeGxpbms6aHJlZj0iI3AiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMwIDApIHNrZXdZKC00MCkiPjwvdXNlPgo8L3N2Zz4=');
  }

  &__face {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    padding: 15px;
  }

  &__value {
    display: block;
    font-size: 18pt;

    &--top {
      align-self: flex-start;
    }

    &--bottom {
      align-self: flex-end;
    }
  }

  &__center {
    display: block;
    font-size: 32pt;
    align-self: center;
  }
}
</style>
