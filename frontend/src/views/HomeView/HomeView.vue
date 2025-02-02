<template>
	<div v-if="!isLoggedIn" class="home__logged-out">
		<Heading tag="h1" headingClass="home__logged-out__title text--primary font--bold">Bienvenido</Heading>
		<Heading tag="h2" headingClass="home__logged-out__subtitle text--black font--regular">¿Qué deseas hacer?</Heading>
		<RouterLink to="/login" class="home__logged-out__link font--bold">Iniciar sesión</RouterLink>
		<RouterLink to="/register" class="home__logged-out__link font--bold">Registrarte</RouterLink>
	</div>
	<div v-else>
		<p>Welcome back!</p>
		<button @click="logout">Logout</button>
	</div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../../components/Heading/Heading.vue'

export default {
	name: 'HomeView',
	components: {
		Heading
	},
	setup() {
		const isLoggedIn = ref(false)
		const router = useRouter()

		onMounted(() => {
			const token = localStorage.getItem('token')
			if (token) {
				isLoggedIn.value = true
			}
		})

		const logout = () => {
			localStorage.removeItem('token')
			isLoggedIn.value = false
			router.push('/login')
		}

		return {
			isLoggedIn,
			logout
		}
	}
}
</script>

<style lang="scss" scoped>
@use './HomeView.scss';
</style>