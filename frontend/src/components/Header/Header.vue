<template>
    <header class="header__container">
        <span class="header__username">Hola, <span class="font--bold">{{ name }}</span></span>
        <button @click="logout" class="header__logout-button">Cerrar sesión</button>
    </header>
</template>

<script>
import { useRouter } from 'vue-router'

export default {
    name: 'Header',
    props: {
        name: {
            type: String,
            required: true
        }
    },
    setup(props) {
        const router = useRouter()

        const logout = () => {
            sessionStorage.removeItem('token')
            router.push('/login')
        }

        return {
            logout
        }
    }
}
</script>

<style lang="scss" scoped>
@use './Header.scss';
</style>