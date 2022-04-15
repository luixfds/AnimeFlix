<template>
  <div>
      <div class="background">
          <div class="blur"></div>
      </div>
      <div class="img-logo"><img src="./../assets/media/animeflix-logo.png" alt=""></div>
      <div class="content">
          <div class="box-login">
              <form action="">
                  <h1>Entrar</h1>
                  <input class="form-field" type="email" placeholder="Email ou número de telefone">
                  <input class="form-field" type="password" placeholder="Senha">
                  <button class="form-field form-btn" type="submit"><strong>Entrar</strong></button>
                  <div class="more">
                    <div class="checkbox">
                        <input type="checkbox" id="check-lembre">
                        <label>Lembre de mim</label>
                    </div>
                    <nuxt-link class="help-link" to="/help">Precisa de ajuda?</nuxt-link>
                  </div>
                  <div class="social-login">
                        <a href="https://auth.nuxtjs.org/providers/facebook/" target="_blank" rel="noopener noreferrer" class="facebook social">
                            <img class="media-img" src="./../assets/media/social-media/facebook.png">
                            <label class="media-label">Facebook</label>
                        </a>
                  </div>
                <div class="register">
                    <label>Novo por aqui?</label>
                    <nuxt-link to="/register">Registre-se!</nuxt-link>
                </div>
              </form>
          </div>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss">
    @import "./../assets/scss/pages/login.scss"
</style>