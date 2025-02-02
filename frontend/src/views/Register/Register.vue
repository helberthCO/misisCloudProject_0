<template>
	<div class="register__container">
		<form class="register__form" @submit.prevent="handleRegister" v-if="!registrationSuccess">
			<Heading tag="h1" headingClass="text--primary font--bold">Bienvenido</Heading>
			<Input id="name" label="Nombre" v-model="name" placeholder="Ingresa tu nombre" minlength="3" required />
			<Input id="lastName" label="Apellido" v-model="last_name" placeholder="Ingresa tu apellido" minlength="3" required />
			<Input id="username" label="Nombre de Usiario" v-model="username"
				placeholder="Ingres tu nombre de usuario" minlength="4" required />
			<Input id="password" type="password" label="Contraseña" v-model="password"
				placeholder="Ingresa tu contraseña" minlength="8" required />
			<Button type="submit">Registrarse</Button>
		</form>
		<div class="register__login" v-if="!registrationSuccess">
			<Heading tag="h3" headingClass="subtitle text--primary font--regular">¿Ya tienes una cuenta?</Heading>
			<RouterLink to="/login">Inicia sesión aquí</RouterLink>
		</div>
		<div v-else class="register__success">
			<Heading tag="h2" headingClass="text--primary font--bold">{{ successMessage }}</Heading>
			<RouterLink to="/login">Inicia sesión aquí</RouterLink>
		</div>
	</div>
</template>

<script>
import Heading from '../../components/Heading/Heading.vue'
import Input from '../../components/Input/Input.vue'
import Button from '../../components/Button/Button.vue'
import Link from '../../components/Link/Link.vue'

export default {
	name: 'Register',
	components: {
		Heading,
		Input,
		Button,
		Link
	},
	data() {
		return {
			name: '',
			last_name: '',
			username: '',
			password: '',
			registrationSuccess: false,
			successMessage: ''
		}
	},
	methods: {
		async handleRegister(event) {
			event.preventDefault();

			const userData = {
				name: this.name,
				last_name: this.last_name,
				username: this.username,
				password: this.password
			}

			try {
				const response = await fetch('http://localhost:8000/register', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify(userData)
				})

				const result = await response.json()
				if (response.ok) {
					this.successMessage = result.message
					this.registrationSuccess = true
				} else {
					console.error('Error:', result.detail)
				}
			} catch (error) {
				console.error('Error:', error)
			}
		}
	}
}
</script>

<style lang="scss" scoped>
@use './Register.scss';
</style>