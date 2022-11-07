

module.exports = {
  devServer: {
    proxy: {
      '/*': {
        target: 'http://web-studio.std-1961.ist.mospolytech.ru/api/v1/',
        changeOrigin: true,
        ws: true
      }
    },
  }
}