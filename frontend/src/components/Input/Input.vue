<template>
    <div class="input-wrapper">
        <label v-if="label" :for="id">{{ label }}</label>
        <input
            :id="id"
            :type="type"
            :placeholder="placeholder"
            :value="modelValue"
            :required="required"
            :minlength="minlength"
            @input="$emit('update:modelValue', $event.target.value)"
        />
    </div>
</template>
  
<script>
  export default {
    name: 'Input',
    props: {
      id: {
        type: String,
        default: null
      },
      type: {
        type: String,
        default: 'text'
      },
      modelValue: {
        type: [String, Number],
        default: ''
      },
      placeholder: {
        type: String,
        default: ''
      },
      label: {
        type: String,
        default: ''
      },
      required: {
        type: Boolean,
        default: false
      },
      minlength: {
        type: Number,
        default: 0
      }
    }
  }
</script>

<style lang="scss" scoped>
@use './Input.scss';
</style>