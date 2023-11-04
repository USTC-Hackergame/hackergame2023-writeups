<script setup lang="ts">
import QQWindow from '@/components/QQChat/QQWindow.vue'

// import ImageMessage from '@/components/QQChat/Message/ImageMessage.vue'
// import QuoteMessage from '@/components/QQChat/Message/QuoteMessage.vue'
// import ForwardMessage from '@/components/QQChat/Message/ForwardMessage.vue'
// import VoiceMessage from '@/components/QQChat/Message/VoiceMessage.vue'
// import FileMessage from '@/components/QQChat/Message/FileMessage.vue'
</script>

<template>
  <QQWindow :title="title" :count="count">
    <!-- Original examples removed -->
    <div v-for="(item, idx) in messages" :key="idx">
      <component :is="item.type" :name="item.name" @revoke="() => revoke(idx)">
        <span v-html="item.message"></span>
      </component>
    </div>
  </QQWindow>
</template>

<script lang="ts">
import axios from 'axios'
import { defineComponent } from 'vue'
import ToastMessage from '@/components/QQChat/Message/ToastMessage.vue'
import NormalMessage from '@/components/QQChat/Message/NormalMessage.vue'

type VueMessage = {
  name: string
  message: string
  type: string
}

type BackendMessage = {
  text: string
  delay: number
}

type BackendResponse = {
  server_starttime: string
  messages: BackendMessage[]
}

export default defineComponent({
  components: {
    NormalMessage: NormalMessage,
    ToastMessage: ToastMessage,
  },
  props: {},
  data() {
    return {
      title: 'Hackergame 202x',
      count: '' as string | number,
      timers: [] as NodeJS.Timeout[],
      messages: [] as VueMessage[],
      fakeContainerElement: null as HTMLElement | null,
      currentScrollHeight: 0,
      stopScroll: false,
    }
  },
  created() {
    const urlParams = new URLSearchParams(window.location.search)
    axios
      .get('/api/checkToken', { params: urlParams })
      .then(() => {
        // 清除 URL 栏的 query
        window.history.replaceState({}, '', '/')
        axios
          .post('/api/getMessages')
          .then((res) => {
            const data = res.data as BackendResponse

            const messages: BackendMessage[] = data.messages
            this.count = messages.length
            for (const message of messages) {
              this.timers.push(
                setTimeout(() => {
                  this.messages.push({
                    name: this.randomString(), // random username
                    message: message.text,
                    type: 'NormalMessage',
                  })
                  this.count = (this.count as number) - 1
                  // wait for DOM render
                  this.$nextTick(() => {
                    // try get fake container element and init onscroll event
                    if (!this.fakeContainerElement) {
                      this.fakeContainerElement = document.querySelector('.fakeqq-container')
                      if (this.fakeContainerElement) {
                        // init onscroll event only once
                        this.fakeContainerElement.onscroll = () => {
                          const offsetHeight = this.fakeContainerElement?.offsetHeight ?? 0
                          const scrollHeight = this.fakeContainerElement?.scrollHeight ?? 0
                          const scrollTop = this.fakeContainerElement?.scrollTop ?? 0
                          if (offsetHeight + scrollTop >= scrollHeight - 10) {
                            this.stopScroll = false
                          } else {
                            this.stopScroll = true
                          }
                        }
                      }
                    }
                    if (!this.stopScroll) {
                      this.currentScrollHeight = this.fakeContainerElement?.scrollHeight ?? 0
                      this.fakeContainerElement?.scrollTo(0, this.currentScrollHeight)
                    }
                  })
                }, message.delay * 1000)
              )
            }

            this.timers.push(
              setTimeout(() => {
                axios
                  .post('/api/getflag')
                  .then((res) => {
                    const data = res.data
                    if (data.success) {
                      alert('恭喜你，flag 是：' + data.flag)
                    } else {
                      alert('获取 flag 失败，原因：' + data.error)
                    }
                  })
                  .catch(() => {
                    alert('网络错误，请刷新页面重新开始')
                  })
              }, messages[messages.length - 1].delay * 1000 + 5000)
            )
          })
          .catch(() => {
            alert('网络错误，请刷新页面重新开始')
          })
      })
      .catch(() => {
        window.location.href = '/api/checkToken'
      })
  },
  beforeUnmount() {
    if (this.timers) {
      for (const timer of this.timers) {
        clearTimeout(timer)
      }
    }
  },
  methods: {
    revoke(idx: number) {
      // this.messages[idx].message = '你撤回了一条消息'
      this.messages[idx].message = '正在撤回...'
      // const original_type = this.messages[idx].type
      this.messages[idx].type = 'ToastMessage'
      axios
        .post('/api/deleteMessage', { id: idx })
        .then((res) => {
          const data = res.data
          if (data.success) {
            this.messages[idx].message = '你撤回了一条消息'
          } else {
            this.messages[idx].message = `撤回失败（${data.error}）`
            // this.messages[idx].type = original_type
          }
        })
        .catch(() => {
          alert('网络错误，请刷新页面重新开始')
        })
    },
    randomString() {
      let result = ''
      const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
      const charactersLength = characters.length
      for (let i = 0; i < 16; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength))
      }
      return result
    },
  },
})
</script>
