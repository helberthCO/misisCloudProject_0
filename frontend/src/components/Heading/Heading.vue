<template>
    <component :is="tag" :class="headingClass">
        <slot></slot>
    </component>
</template>

<script>
export default {
    name: 'Heading',
    props: {
        tag: {
            type: String,
            default: 'h1'
        },
        headingClass: {
            type: String,
            default: ''
        }
    }
}
</script>

<style lang="scss" scoped>
@use './Heading.scss';
</style>