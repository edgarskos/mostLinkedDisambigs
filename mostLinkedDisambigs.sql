select count(*) from pagelinks where pl_title in (select page_title from page where page_id in (select cl_from from categorylinks where cl_to="Wikipedie:Rozcestníky")) group by pl_title
