---
title: 也谈WordPress说说/微博功能
url: https://h4ck.org.cn/2023/03/%e4%b9%9f%e8%b0%88wordpress%e8%af%b4%e8%af%b4-%e5%be%ae%e5%8d%9a%e5%8a%9f%e8%83%bd/
source: obaby@mars
date: 2023-03-29
fetch_date: 2025-10-04T10:58:16.667728
---

# 也谈WordPress说说/微博功能

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 也谈WordPress说说/微博功能

2023年3月28日
[20 条评论](https://h4ck.org.cn/2023/03/11659#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/8cf511909ef4213a9add7e314a09000e.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/8cf511909ef4213a9add7e314a09000e.jpg)

姐姐做事情一向不喜欢从头开始搞，~~主要是水平太菜，搞php真的是不专业。~~于是就只能到处抄作业了。好在wp算是使用比较广泛的系统，相对来说查找各种资料还不算太麻烦，但是国内的互联网环境嘛，就一言难尽了。各种抄作业，基本是一篇文章被搬到了不同的地方。可能很多人连尝试都没尝试就抄过去了，但是姐姐不一样啊。姐姐的作业是要实际测试的。

之前看[杜老师](https://dusays.com)弄的说说还是蛮不错的，基于memos。不过个人觉得总有点遗憾，那就是两个系统是独立的，账号不互通。另外一个问题就是自己的这个说说模块基本都是自己用，也没有太大的必要搞多用户。于是就想着找找各种插件，测试了不少插件之后，最终觉得Simple microblogging这款插件基本能够满足需求。

不过在使用的过程中也发现了几个问题：

1.页面排版有点另类，具体可以直接安装插件后创建文章查看，横向排版，标题文字图片一排。

2.文章加载要么加载固定条数，要么全部加载，这个设置对于有强迫症的我不太友好

3.没有分页

昨晚用虚拟机上的wp改了一晚上，最终页面样式改的自己多少能看的过去了

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/Jietu20230328-092545.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/Jietu20230328-092545.jpg)

但是分页的问题确实搞不定了，当时就想放弃了。主要是对于wp的各种函数也不熟悉啊，真是让人头大。于是想着淘宝上找个人给改一下：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/WechatIMG5.jpeg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/WechatIMG5.jpeg) [![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/WechatIMG6.jpeg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/WechatIMG6.jpeg)

奈何对面小哥哥回消息有点慢，在等待的过程中姐姐把分页的问题给解决了。

于是现在基本就可以用了，效果嘛最起码自己看的过去了。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/Jietu20230328-093407.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/Jietu20230328-093407.jpg)

安装插件之后修改插件代码，直接复制下面的代码即可：

```
<?php
/*
 * Plugin Name: Simple microblogging
 * Description: Use your wordpress site as a microblog; display the microposts in a widget or using a shortcode.
 * Version: 0.1
 * Author: Samuel Coskey, Victoria Gitman
 * Author URI: http://boolesrings.org
*/
/*
https://www.qiniu.com/qfans/qnso-21193676#comments
*/

// 处理分页
function remove_page_from_query_string($query_string)
{
    if (isset($query_string['name']) && $query_string['name'] == 'page' && isset($query_string['page'])) {
        unset($query_string['name']);
        // 'page' in the query_string looks like '/2', so i'm spliting it out
        @list($delim, $page_index) = explode('/', $query_string['page']);
        $query_string['paged'] = $page_index;
    }
    return $query_string;
}
// I will kill you if you remove this. I died two days for this line
add_filter('request', 'remove_page_from_query_string');

// following are code adapted from Custom Post Type Category Pagination Fix by jdantzer
function fix_category_pagination($qs){
    if(isset($qs['category_name']) && isset($qs['paged'])){
        $qs['post_type'] = get_post_types($args = array(
            'public' => true,
            '_builtin' => false
        ));
        array_push($qs['post_type'],'post');
    }
    return $qs;
}
add_filter('request', 'fix_category_pagination');

/*
 * Create the new post type
*/
add_action( 'init', 'create_micropost_type' );
function create_micropost_type() {
 register_post_type( 'micropost',
  array(
   'labels' => array(
    'name' => __( 'Microposts' ),
    'singular_name' => __( 'Micropost' ),
   ),
   'has_archive' => true,
   'menu_icon' => plugins_url( 'microblogging-icon.png', __FILE__ ),
   'menu_position' => 5,
   'public' => true,
   'rewrite' => array( 'slug' => 'microposts' ),
   'supports' => array( 'title', 'editor', 'author', 'comments' ),
// uncomment to support categories and tags:
 'taxonomies' => array ( 'category', 'post_tag' ),
  )
 );
}
/*
 * Tells wordpress to reset its permalink structure, to accommodate the new post type
*/
register_activation_hook( __FILE__, 'my_rewrite_flush' );
function my_rewrite_flush()
{
 create_micropost_type();
 flush_rewrite_rules();
}
/*
 * Microblog widget code
*/
add_action('widgets_init', 'ahspfc_load_widgets');
function ahspfc_load_widgets() {
 register_widget('microblog_widget');
}
class microblog_widget extends WP_Widget {
 function microblog_widget() {
  $widget_ops = array(
   'classname' => 'microblog_widget',
   'description' => 'Allows you to display a list of microblog entries while excluding them from posts.',
  );
  $control_ops = array(
   'id_base' => 'microblog-widget',
  );
  $this->WP_Widget('microblog-widget', 'Microblog', $widget_ops, $control_ops );
 }
 function form ($instance) {
  $defaults = array(
   'numberposts' => '5',
   'title' => '',
   'rss' => '',
  );
  $instance = wp_parse_args( (array) $instance, $defaults );
?>
  <p>
    <label for="<?php echo $this->get_field_id('title'); ?>">Title:</label>
    <input type="text" name="<?php echo $this->get_field_name('title') ?>" id="<?php echo $this->get_field_id('title') ?> " value="<?php echo $instance['title'] ?>" size="20">
  </p>
  <p>
   <label for="<?php echo $this->get_field_id('numberposts'); ?>">Number of posts:</label>
   <input type="text" name="<?php echo $this->get_field_name('numberposts'); ?>" id="<?php echo $this->get_field_id('numberposts'); ?>" value="<?php echo $instance['numberposts']; ?>">
  </p>
  <p>
   <input type="checkbox" id="<?php echo $this->get_field_id('use_excerpt'); ?>" name="<?php echo $this->get_field_name('use_excerpt'); ?>" <?php if ($instance['use_excerpt']) echo 'checked="checked"' ?> />
   <label for="<?php echo $this->get_field_id('use_excerpt'); ?>">Show excerpts only?</label>
  </p>
  <p>
   <input type="checkbox" id="<?php echo $this->get_field_id('rss'); ?>" name="<?php echo $this->get_field_name('rss'); ?>" <?php if ($instance['rss']) echo 'checked="checked"' ?> />
   <label for="<?php echo $this->get_field_id('rss'); ?>">Show RSS feed link?</label>
  </p>
<?php
 }
 function update ($new_instance, $old_instance) {
  $instance = $old_instance;
  $instance['title'] = $new_instance['title'];
  $instance['numberposts'] = $new_instance['numberposts'];
  $instance['use_excerpt'] = $new_instance['use_excerpt'];
  $instance['rss'] = $new_instance['rss'];
  return $instance;
 }
 function widget ($args,$instance) {
  extract($args);
  $title = $instance['title'];
  $numberposts = $instance['numberposts'];
  $use_excerpt = $instance['use_excerpt'];
  $rss = $instance['rss'];
  // retrieve posts information from database
  global $post;
  $query = "post_type=micropost&posts_per_page=" . $numberposts;
  $query_results = new WP_Query($query);
  // build the widget contents!
  $out = "<ul>";
  while ( $query_results->have_posts() ) {
   $query_results->the_post();
   $out .= "<li>";
   $post_title = the_title( '', '', false );
   if ( $post_title ) {
    $out .= "<span class='microblog-widget-post-title'>"
          . $post_title
          . " </span>";
   }
   $out .= "<span class='microblog-widget-post-content'>";
   if ( $use_excerpt ) {
    add_filter('excerpt_more', 'micropost_excerpt_more');
    $out .= get_the_excerpt();
    remove_filter('excerpt_more', 'micropost_excerpt_more');
   } else {
    $out .= $post->post_content;
   }
   $out .= "</span>";
   $out .= "<span lass='microblog-widget-commentlink'>";
   $out .= " <a href='" . get_permalink() . "'>";
   $out .= "<img width='14px' src='"
         . site_url() . "/wp-includes/images/wlw/wp-comments.png'>";
   $out .= "&times;" . get_comments_number();
   $out .= '</a>';
   $out .= "</s...