<template>
    <button
      :id="id"
      :type="type"
      :disabled="disabled"
      @click="$emit('click', $event)"
      :class="buttonClass"
    >
      <slot></slot>
    </button>
</template>
  
<script>
export default {
    name: 'Button',
    props: {
        id: {
            type: String,
            default: null
        },
        type: {
            type: String,
            default: 'button'
        },
        disabled: {
            type: Boolean,
            default: false
        },
        buttonClass: {
            type: String,
            default: ''
        }
    }
}
</script>

<style lang="scss" scoped>
@use './Button.scss';
</style>