<?php

use Twig\Environment;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Markup;
use Twig\Sandbox\SecurityError;
use Twig\Sandbox\SecurityNotAllowedTagError;
use Twig\Sandbox\SecurityNotAllowedFilterError;
use Twig\Sandbox\SecurityNotAllowedFunctionError;
use Twig\Source;
use Twig\Template;

/* @PrestaShop/Admin/Configure/AdvancedParameters/Backup/download_view.html.twig */
class __TwigTemplate_8b4168ea0eed5b5099f960a2b91cfea4e8c6d62db38c790a86549cc078d6d0bc extends \Twig\Template
{
    public function __construct(Environment $env)
    {
        parent::__construct($env);

        $this->blocks = [
            'content' => [$this, 'block_content'],
        ];
    }

    protected function doGetParent(array $context)
    {
        // line 25
        return "@PrestaShop/Admin/layout.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = [])
    {
        $__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e->enter($__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e_prof = new \Twig\Profiler\Profile($this->getTemplateName(), "template", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/download_view.html.twig"));

        $__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02->enter($__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02_prof = new \Twig\Profiler\Profile($this->getTemplateName(), "template", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/download_view.html.twig"));

        $this->parent = $this->loadTemplate("@PrestaShop/Admin/layout.html.twig", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/download_view.html.twig", 25);
        $this->parent->display($context, array_merge($this->blocks, $blocks));
        
        $__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e->leave($__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e_prof);

        
        $__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02->leave($__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02_prof);

    }

    // line 29
    public function block_content($context, array $blocks = [])
    {
        $__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e = $this->env->getExtension("Symfony\\Bundle\\WebProfilerBundle\\Twig\\WebProfilerExtension");
        $__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e->enter($__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e_prof = new \Twig\Profiler\Profile($this->getTemplateName(), "block", "content"));

        $__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02 = $this->env->getExtension("Symfony\\Bridge\\Twig\\Extension\\ProfilerExtension");
        $__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02->enter($__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02_prof = new \Twig\Profiler\Profile($this->getTemplateName(), "block", "content"));

        // line 30
        echo "  <div class=\"container-fluid\">
    <div class=\"row\">
      <div class=\"col\">
        <div class=\"card\">
          <h3 class=\"card-header\">
            <i class=\"material-icons\">cloud_download</i>
            ";
        // line 36
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Download", [], "Admin.Actions"), "html", null, true);
        echo "
          </h3>
          <div class=\"card-body\">
            <div class=\"alert alert-success\" role=\"alert\">
              <p class=\"alert-text\">
                ";
        // line 41
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Beginning the download ...", [], "Admin.Advparameters.Notification"), "html", null, true);
        echo "
              </p>
            </div>
            <p>
              ";
        // line 45
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Backup files should automatically start downloading.", [], "Admin.Advparameters.Notification"), "html", null, true);
        echo "
              ";
        // line 46
        echo $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("If not,[1][2] please click here[/1]!", ["[1]" => ((" <a href=\"" . $this->getAttribute(($context["downloadFile"] ?? $this->getContext($context, "downloadFile")), "url", [])) . "\" class=\"btn btn-outline-primary btn-sm\">"), "[/1]" => "</a> ", "[2]" => "<i class=\"icon-download\"></i>"], "Admin.Advparameters.Notification");
        echo "
          </p>
          <p class=\"mb-0\">
            <a class=\"btn btn-outline-primary btn-sm\" href=\"";
        // line 49
        echo $this->env->getExtension('Symfony\Bridge\Twig\Extension\RoutingExtension')->getPath("admin_backups_index");
        echo "\">
              <i class=\"material-icons\">keyboard_backspace</i>
              ";
        // line 51
        echo twig_escape_filter($this->env, $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Back to list", [], "Admin.Actions"), "html", null, true);
        echo "
            </a>
          </p>
            <iframe src=\"";
        // line 54
        echo twig_escape_filter($this->env, $this->getAttribute(($context["downloadFile"] ?? $this->getContext($context, "downloadFile")), "url", []), "html", null, true);
        echo "\" class=\"d-none\"></iframe>
          </div>
        </div>
      </div>
    </div>
  </div>
";
        
        $__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02->leave($__internal_319393461309892924ff6e74d6d6e64287df64b63545b994e100d4ab223aed02_prof);

        
        $__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e->leave($__internal_085b0142806202599c7fe3b329164a92397d8978207a37e79d70b8c52599e33e_prof);

    }

    public function getTemplateName()
    {
        return "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/download_view.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  104 => 54,  98 => 51,  93 => 49,  87 => 46,  83 => 45,  76 => 41,  68 => 36,  60 => 30,  51 => 29,  29 => 25,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Source("{#**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Open Software License (OSL 3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/OSL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)
 *#}
{% extends '@PrestaShop/Admin/layout.html.twig' %}

{% trans_default_domain 'Admin.Advparameters.Feature' %}

{% block content %}
  <div class=\"container-fluid\">
    <div class=\"row\">
      <div class=\"col\">
        <div class=\"card\">
          <h3 class=\"card-header\">
            <i class=\"material-icons\">cloud_download</i>
            {{ 'Download'|trans({}, 'Admin.Actions') }}
          </h3>
          <div class=\"card-body\">
            <div class=\"alert alert-success\" role=\"alert\">
              <p class=\"alert-text\">
                {{ 'Beginning the download ...'|trans({}, 'Admin.Advparameters.Notification') }}
              </p>
            </div>
            <p>
              {{ 'Backup files should automatically start downloading.'|trans({}, 'Admin.Advparameters.Notification') }}
              {{ 'If not,[1][2] please click here[/1]!'|trans({'[1]': ' <a href=\"'~ downloadFile.url ~'\" class=\"btn btn-outline-primary btn-sm\">', '[/1]': '</a> ', '[2]': '<i class=\"icon-download\"></i>'}, 'Admin.Advparameters.Notification')|raw }}
          </p>
          <p class=\"mb-0\">
            <a class=\"btn btn-outline-primary btn-sm\" href=\"{{ path('admin_backups_index') }}\">
              <i class=\"material-icons\">keyboard_backspace</i>
              {{ 'Back to list'|trans({}, 'Admin.Actions') }}
            </a>
          </p>
            <iframe src=\"{{ downloadFile.url }}\" class=\"d-none\"></iframe>
          </div>
        </div>
      </div>
    </div>
  </div>
{% endblock %}
", "@PrestaShop/Admin/Configure/AdvancedParameters/Backup/download_view.html.twig", "/var/www/html/src/PrestaShopBundle/Resources/views/Admin/Configure/AdvancedParameters/Backup/download_view.html.twig");
    }
}
