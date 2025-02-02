<template>
  <div>
    <RouterLink v-if="to" :to="to" :class="linkClass">
      <slot></slot>
    </RouterLink>
    <a v-else :href="href" :class="linkClass">
      <slot></slot>
    </a>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router'

export default {
  name: 'Link',
  components: {
    RouterLink
  },
  props: {
    to: {
      type: String,
      default: null
    },
    href: {
      type: String,
      default: '#'
    },
    linkClass: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss" scoped>
@use './Link.scss';
</style>