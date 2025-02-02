<template>
	<div class="login__container">
		<form class="login__sign-in" @submit.prevent="handleClick" v-if="!loginSuccess">
			<Heading tag="h1" headingClass="text--black font--medium">Inicia sesión</Heading>
			<Input 
                id="username" 
                label="Nombre de usuario" 
                v-model="username" 
                :class="{ 'error': userNotFound }" 
                placeholder="Ingresa tu nombre de usuario"
				required
            />
			<p v-if="userNotFound" class="error">{{ userNotFoundMessage }}</p>
            <Input 
                id="password" 
                type="password" 
                label="Contraseña" 
                v-model="password" 
                :class="{ 'error': invalidPassword }" 
                placeholder="Ingresa tu contraseña"
				required
            />
			<p v-if="invalidPassword" class="error">{{ invalidPasswordMessage }}</p>
			<Button type="submit">Ingresar</Button>
		</form>
		<div class="login__register" v-if="!loginSuccess">
			<Heading tag="h2" headingClass="title text--white font--bold">Bienvenido!</Heading>
			<Heading tag="h3" headingClass="subtitle text--white font--regular">¿No tienes una cuenta?</Heading>
			<RouterLink to="/register" class="text--white">Registrate aquí</RouterLink>
		</div>
		<div v-else class="login__success">
			<Heading tag="h2" headingClass="text--primary font--bold">{{ loginMessage }}</Heading>
		</div>
	</div>
</template>


<script>
import Heading from '../../components/Heading/Heading.vue'
import Input from '../../components/Input/Input.vue'
import Button from '../../components/Button/Button.vue'
import Link from '../../components/Link/Link.vue'

export default {
	name: 'Login',
	components: {
		Heading,
		Input,
		Button,
		Link
	},
	data() {
		return {
			username: '',
			password: '',
			loginSuccess: false,
			userNotFound: false,
			invalidPassword: false,
			loginMessage: '',
			userNotFoundMessage: '',
			invalidPasswordMessage: ''
		}
	},
	methods: {
		async handleClick(event) {
			event.preventDefault();

			const loginData = {
				username: this.username,
				password: this.password
			}

			try {
				const response = await fetch('http://localhost:8000/login', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify(loginData)
				})

				const result = await response.json()
				
				if (response.ok) {
					this.loginMessage = result.message
					this.loginSuccess = true
					console.log(response);
					
					sessionStorage.setItem('first_name', result.name)
					sessionStorage.setItem('last_name', result.last_name)
					sessionStorage.setItem('token', result.access_token)
					this.$router.push('/')
				} else if (response.status === 404) {
					this.userNotFoundMessage = result.detail
					this.userNotFound = true
				} else if (response.status === 400) {
					this.invalidPasswordMessage = result.detail
					this.invalidPassword = true
				} else {
					console.error('Error:', result.message)
				}
			} catch (error) {
				console.error('Error:', error)
			}
		}
	}
}
</script>

<style lang="scss" scoped>
@use './Login.scss';
</style>