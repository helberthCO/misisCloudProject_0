<template>
	<Header v-if="isLoggedIn" :name="fullName" />
	<div v-else class="home__logged-out">
		<Heading tag="h1" headingClass="home__logged-out__title text--primary font--bold">Bienvenido</Heading>
		<Heading tag="h2" headingClass="home__logged-out__subtitle text--black font--regular">¿Qué deseas hacer?</Heading>
		<RouterLink to="/login" class="home__logged-out__link font--bold">Iniciar sesión</RouterLink>
		<RouterLink to="/register" class="home__logged-out__link font--bold">Registrarte</RouterLink>
	</div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../../components/Heading/Heading.vue'
import Header from '../../components/Header/Header.vue'

export default {
	name: 'HomeView',
	components: {
		Heading,
		Header
	},
	setup() {
		const isLoggedIn = ref(false)
		let firstName = ref('')
		let lastName = ref('')
		const router = useRouter()

		onMounted(() => {
			const token = sessionStorage.getItem('token')
			firstName = sessionStorage.getItem('first_name')
			lastName = sessionStorage.getItem('last_name')
			
			if (token) {
				isLoggedIn.value = true
			}
		})

		const logout = () => {
			sessionStorage.removeItem('token')
			sessionStorage.removeItem('first_name')
			sessionStorage.removeItem('last_name')
			isLoggedIn.value = false
			router.push('/login')
		}

		const fullName = computed(() => `${firstName} ${lastName}`)

		return {
			isLoggedIn,
			fullName,
			logout
		}
	}
}
</script>

<style lang="scss" scoped>
@use './HomeView.scss';
</style>