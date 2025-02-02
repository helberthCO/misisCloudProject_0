module.exports = {
  devServer: {
    proxy: {
      '/register': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: { '^/register': '/register' }
      },
      '/login': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: { '^/login': '/login' }
      }
    }
  }
}