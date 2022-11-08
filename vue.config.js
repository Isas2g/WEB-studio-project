

module.exports = {
  devServer: {
    proxy: {
      '/api/v1/*': {
        target: 'http://web-studio.std-1961.ist.mospolytech.ru/',
        changeOrigin: true,
        ws: true
      }
    },
  }
}